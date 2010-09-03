%define upstream_name	 URI
%define upstream_version 1.55

%define _requires_exceptions perl(Business::ISBN)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	URI module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/URI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	rpm-build >= 4.2-7mdk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module implements the URI class. Objects of this class represent
Uniform Resource Identifier (URI) references as specified in RFC 2396.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc Changes README
%{perl_vendorlib}/URI.pm
%{perl_vendorlib}/URI
%{_mandir}/*/*
