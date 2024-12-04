%define modname	URI

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Business::ISBN\\)'
%else
%define _requires_exceptions perl(Business::ISBN)
%endif

%bcond_without test

Summary:	URI module for perl
Name:		perl-%{modname}
Version:	5.31
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/URI
Source0:	https://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/URI-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl-devel
BuildRequires:	perl(JSON::PP)
%if %{with tests}
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(Test::Fatal)
%endif

%description
This Perl module implements the URI class. Objects of this class represent
Uniform Resource Identifier (URI) references as specified in RFC 2396.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Deal with the fact that we have a newer version of perl(Exporter)
# than the hardcoded dep...

find . -type f |xargs sed -i -e 's,5\.57,5.77,g'

perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%if %{with tests}
%check
%make test
%endif

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/URI.pm
%{perl_vendorlib}/URI
%{_mandir}/man3/*
