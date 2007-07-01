%define module	Lingua-Stem-It
%define name	perl-%{module}
%define version 0.02
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Porter's stemming algorithm for Italian
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AC/ACALPINI/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module applies the Porter Stemming Algorithm to its parameters, returning
the stemmed words.

The algorithm is implemented exactly as described in:
http://snowball.tartarus.org/italian/stemmer.html

The code is carefully crafted to work in conjunction with the Lingua::Stem
module by Benjamin Franz, from which some functionalities have been borrowed
(caching and exception list).

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*

