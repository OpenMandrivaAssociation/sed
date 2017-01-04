%define debug_package %{nil}
# (tpg) fails 2017-01-04
# /tmp/lto-llvm-4c8404.o:ld-temp.o:function compile_regex_1: error: undefined reference to '__muloti4'
%define _disable_lto 1

Summary:	A GNU stream text editor
Name:		sed
Version:	4.3
Release:	1
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.xz
BuildRequires:	acl-devel
BuildRequires:	texinfo
Provides:	/bin/sed

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -q
%apply_patches

%build
%configure	\
    --bindir=/bin \
    --without-included-regex \
    --with-packager="%{vendor}" \
    --with-packager-version="%{distro_release}" \
    --with-packager-bug-reports="%{disturl}"

%make LDFLAGS=-s
%make html

#(tpg) disable checks
#check
#make check

%install
%makeinstall_std
rm -f %{buildroot}%{_docdir}/sed.html

%find_lang %{name}

%files -f %{name}.lang
%doc BUGS NEWS README doc/sed.html
%attr(755,root,root) /bin/sed
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1*
