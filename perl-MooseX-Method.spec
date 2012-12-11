%define upstream_name    MooseX-Method
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Method declaration with type checking
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Template::Pro)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildArch:	noarch

%description
The problem
    This module is an attempt to solve a problem I've often encountered but
    never really found any good solution for: validation of method
    parameters. How many times have we all ourselves writing code like
    this:

      sub foo {
        my ($self,$args) = @_;

        die "Invalid arg1"
          unless (defined $arg->{bar} && $arg->{bar} =~ m/bar/);
      }

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
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.0
+ Revision: 405945
- rebuild using %%perl_convert_version

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2010.0
+ Revision: 391186
- update to new version 0.44

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2010.0
+ Revision: 387013
- update to new version 0.43

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2009.0
+ Revision: 235686
- import perl-MooseX-Method


* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2009.0
- initial mdv release, generated with cpan2dist
