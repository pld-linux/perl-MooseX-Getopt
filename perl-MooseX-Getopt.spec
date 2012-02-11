#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Getopt
Summary:	MooseX::Getopt - A Moose role for processing command line options
Summary(pl.UTF-8):	MooseX::Getopt - narzędzie Moose do przetwarzania opcji z linii komend
Name:		perl-MooseX-Getopt
Version:	0.39
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f4e6ffb5794335eb6222dd822357687a
URL:		http://search.cpan.org/dist/MooseX-Getopt/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:	perl-Moose >= 0.56
BuildRequires:	perl-MooseX-Role-Parameterized
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Requires
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a role which provides an alternate constructor for creating
objects using parameters passed in from the command line.

This module attempts to DWIM as much as possible with the command line
params by introspecting your class's attributes. It will use the name
of your attribute as the command line option, and if there is a type
constraint defined, it will configure Getopt::Long to handle the
option accordingly.

You can use the trait MooseX::Getopt::Meta::Attribute::Trait or the
attribute metaclass MooseX::Getopt::Meta::Attribute to get non-default
commandline option names and aliases.

You can use the trait MooseX::Getopt::Meta::Attribute::Trait::NoGetopt
or the attribute metaclass MooseX::Getopt::Meta::Attribute::NoGetopt
to have MooseX::Getopt ignore your attribute in the commandline
options.

%description -l pl.UTF-8
Jest to narzędzie które dostarcza alternatywny konstruktor do
tworzenia objektówkorzystających z parametrów przekazanych z linii
poleceń.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/Getopt
%{_mandir}/man3/*
