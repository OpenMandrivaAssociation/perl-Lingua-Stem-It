%define upstream_name	 Lingua-Stem-It
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Porter's stemming algorithm for Italian
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AC/ACALPINI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module applies the Porter Stemming Algorithm to its parameters, returning
the stemmed words.

The algorithm is implemented exactly as described in:
http://snowball.tartarus.org/italian/stemmer.html

The code is carefully crafted to work in conjunction with the Lingua::Stem
module by Benjamin Franz, from which some functionalities have been borrowed
(caching and exception list).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 403390
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2009.0
+ Revision: 257597
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 245628
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-1mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2008.0
+ Revision: 46531
- update to new version 0.02


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdv2007.0
- Rebuild

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdk
- spec cleanup
- better summary
- better description
- better url
- rpmbuildupdate aware
- %%mkrel

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.01-2mdk
- fix deps

