%define debug_package %{nil}

Summary:	A GNU stream text editor
Name:		sed
Version:	4.2.1
Release:	7
License:	GPL
Group:		Text tools
Url:		http://www.gnu.org/software/sed/
Source0:	ftp://ftp.gnu.org/pub/gnu/sed/%{name}-%{version}.tar.bz2
Patch0:		sed-4.1.1-dest_len-0.1.patch
Provides: /bin/sed
BuildRequires:	texinfo

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -q
%patch0 -p1 -b .dest_len

%build
%configure2_5x	--bindir=/bin
%make LDFLAGS=-s
%make html
%make check

%install
%makeinstall_std
rm -f %{buildroot}%{_docdir}/sed.html

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS NEWS README doc/sed.html
%attr(755,root,root) /bin/sed 
%{_infodir}/sed.info*
%{_mandir}/man1/sed.1*




%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 4.2.1-4mdv2011.0
+ Revision: 669967
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.1-3mdv2011.0
+ Revision: 607530
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.1-2mdv2010.1
+ Revision: 520215
- rebuilt for 2010.1

* Sun Jun 28 2009 Frederik Himpe <fhimpe@mandriva.org> 4.2.1-1mdv2010.0
+ Revision: 390170
- update to new version 4.2.1

* Sat May 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.2-1mdv2010.0
+ Revision: 370724
- update to new version 4.2

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 4.1.5-5mdv2009.1
+ Revision: 317154
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.1.5-4mdv2009.0
+ Revision: 225433
- rebuild

* Fri Jan 04 2008 Emmanuel Andry <eandry@mandriva.org> 4.1.5-3mdv2008.1
+ Revision: 144218
- Fix group (bug #36363)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.1.5-2mdv2007.0
+ Revision: 119972
- Import sed

* Wed Mar 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.1.5-1mdk
- 4.1.5
- Fix prereq

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 4.1.4-3mdk
- Rebuild

* Sat Feb 19 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 4.1.4-2mdk
- add BuildRequires: texinfo

* Fri Feb 18 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.1.4-1mdk
- 4.1.4
- fix summary-ended-with-dot
- rather specify bindir with configure than moving it around afterwards

* Wed Nov 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.1.2-1mdk
- 4.1.2

* Thu Aug 19 2004 Stew Benedict <sbenedict@mandrakesoft.com> 4.1.1-2mdk
- new patch0 for lsb/i18n tests (Mitsuru Chinen, should merge upstream soon)

* Tue Jul 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.1.1-1mdk
- 4.1.1
- cosmetics

