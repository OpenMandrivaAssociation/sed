%define debug_package %{nil}
# (tpg) fails 2017-01-04
# /tmp/lto-llvm-4c8404.o:ld-temp.o:function compile_regex_1: error: undefined reference to '__muloti4'
%global optflags %{optflags} -O3 -rtlib=compiler-rt

Summary:	A GNU stream text editor
Name:		sed
Version:	4.5
Release:	1
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.xz
Patch0:		sed-4.5-check-for-__builtin_mul_overflow_p.patch
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
%autopatch -p1

%build
%configure \
    --bindir=/bin \
    --without-included-regex \
    --with-packager="%{vendor}" \
    --with-packager-version="%{distro_release}" \
    --with-packager-bug-reports="%{disturl}"

%make_build LDFLAGS=-s

#(tpg) disable checks
#check
#make check

%install
%make_install
rm -f %{buildroot}%{_docdir}/sed.html

%find_lang %{name}

%files -f %{name}.lang
%doc BUGS NEWS README
%attr(755,root,root) /bin/sed
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1*
