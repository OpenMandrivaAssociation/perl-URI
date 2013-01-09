%define upstream_name	 URI
%define upstream_version 1.58

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Business::ISBN\\)'
%else
%define _requires_exceptions perl(Business::ISBN)
%endif

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:	URI module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildArch:	noarch

%description
This Perl module implements the URI class. Objects of this class represent
Uniform Resource Identifier (URI) references as specified in RFC 2396.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/URI.pm
%{perl_vendorlib}/URI
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.580.0-5mdv2012.0
+ Revision: 765801
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.580.0-4
+ Revision: 764324
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.580.0-3
+ Revision: 763115
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.580.0-2
+ Revision: 667405
- mass rebuild

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.580.0-1
+ Revision: 635556
- update to new version 1.58

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2011.0
+ Revision: 596680
- update to 1.56

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.550.0-1mdv2011.0
+ Revision: 575598
- update to 1.55

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.540.0-1mdv2011.0
+ Revision: 530377
- update to 1.54

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.530.0-1mdv2010.1
+ Revision: 519959
- update to 1.53

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.520.0-1mdv2010.1
+ Revision: 484375
- update to 1.52

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.510.0-1mdv2010.1
+ Revision: 469440
- update to 1.51

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2010.1
+ Revision: 468893
- update to 1.50

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 416975
- update to 1.40

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.380.0-1mdv2010.0
+ Revision: 406386
- rebuild using %%perl_convert_version

* Fri Jul 17 2009 Götz Waschk <waschk@mandriva.org> 1.38-2mdv2010.0
+ Revision: 396871
- rebuild

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2010.0
+ Revision: 383546
- update to new version 1.38

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.37-2mdv2009.1
+ Revision: 351693
- rebuild

* Tue Jun 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.37-1mdv2009.0
+ Revision: 222661
- update to new version 1.37

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2009.0
+ Revision: 194958
- update to new version 1.36

* Tue Jan 22 2008 Jérôme Quelin <jquelin@mandriva.org> 1.35-5mdv2008.1
+ Revision: 156499
- force rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:42:34 (63281)
- rebuild

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:11:07 (62908)
- Import perl-URI

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 1.35-3mdk
- Add %%{1}mdv2007.1
- Updated BuildRequires
- Updated to comply with Mandriva perl packaging policies

* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.35-2mdk
- Rebuild, remove MANIFEST

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.35-1mdk
- New version 1.35
- Reenable 'make test'

* Sat Sep 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.31-3mdk
- Disable 'make test', due to an heuristic.t test failure

* Wed Jul 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.31-2mdk
- Update description

* Wed Jun 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.31-1mdk
- 1.31.

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.30-1mdk
- 1.30.

