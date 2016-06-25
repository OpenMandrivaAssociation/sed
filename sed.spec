%define debug_package %{nil}

Summary:	A GNU stream text editor
Name:		sed
Version:	4.2.2
Release:	17
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.bz2.sig
Patch0:		sed-4.1.1-dest_len-0.1.patch
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
    --without-included-regex

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
