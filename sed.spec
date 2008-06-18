Summary:	A GNU stream text editor
Name:		sed
Version:	4.1.5
Release:	%mkrel 4
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.bz2
Patch0:		sed-4.1.1-dest_len-0.1.patch
Requires(pre):	info-install
BuildRequires:	texinfo
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -q
%patch -p1 -b .dest_len

%build
%configure2_5x	--bindir=/bin
%make LDFLAGS=-s
%make html
%make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
rm -f %{buildroot}%{_docdir}/sed.html

%find_lang %{name}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS NEWS README doc/sed.html
%attr(755,root,root) /bin/sed 
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1*


