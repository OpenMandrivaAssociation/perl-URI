%define _requires_exceptions perl(Business::ISBN)

%define module	URI

Summary:	URI module for perl
Name:		perl-%{module}
Version:	1.35
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/%{module}-%{version}.tar.bz2
BuildRequires:	perl
BuildRequires:	rpm-build >= 4.2-7mdk
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This Perl module implements the URI class. Objects of this class represent
Uniform Resource Identifier (URI) references as specified in RFC 2396.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README rfc2396.txt
%{perl_vendorlib}/URI.pm
%{perl_vendorlib}/URI
%{_mandir}/*/*


