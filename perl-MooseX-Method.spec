%define module   MooseX-Method
%define version    0.42
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Method declaration with type checking
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
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
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

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

