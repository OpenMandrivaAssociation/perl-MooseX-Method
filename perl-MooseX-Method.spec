%define upstream_name    MooseX-Method
%define upstream_version 0.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Method declaration with type checking
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Template::Pro)
BuildRequires: perl(Moose)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/MooseX
