%define debug_package %{nil}
%global optflags %{optflags} -Oz

Summary:	A GNU stream text editor
Name:		sed
Version:	4.9
Release:	2
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.xz
Patch0:		sed-4.9-clang.patch
BuildRequires:	pkgconfig(libacl)
BuildRequires:	texinfo
Provides:	/bin/sed

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%autosetup -p1

%build
%configure \
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
%attr(755,root,root) %{_bindir}/sed
%doc %{_infodir}/sed.info*
%doc %{_mandir}/man1/sed.1*
