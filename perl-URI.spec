%define modname	URI
%define modver 1.74

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Business::ISBN\\)'
%else
%define _requires_exceptions perl(Business::ISBN)
%endif

Summary:	URI module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/URI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl-devel
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Test::Needs)

%description
This Perl module implements the URI class. Objects of this class represent
Uniform Resource Identifier (URI) references as specified in RFC 2396.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/URI.pm
%{perl_vendorlib}/URI
%{_mandir}/man3/*
