#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	MooseX
%define	pnam	Getopt
Summary:	MooseX::Getopt - A Moose role for processing command line options
Summary(pl.UTF-8):	MooseX::Getopt - narzędzie Moose do przetwarzania opcji z linii poleceń
Name:		perl-MooseX-Getopt
Version:	0.78
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d0ace976fe24b98f7da3a93a4c4eb87
URL:		https://metacpan.org/dist/MooseX-Getopt
BuildRequires:	perl-Module-Build-Tiny >= 0.034
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Getopt-Long >= 2.37
BuildRequires:	perl-Getopt-Long-Descriptive >= 0.088
BuildRequires:	perl-Module-Metadata
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Moose >= 0.56
BuildRequires:	perl-MooseX-Role-Parameterized >= 1.01
BuildRequires:	perl-Path-Tiny >= 0.009
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Trap
BuildRequires:	perl-Test-Warnings >= 0.009
BuildRequires:	perl-Test2-Suite
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-namespace-autoclean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a role which provides an alternate constructor for creating
objects using parameters passed in from the command line.

%description -l pl.UTF-8
Jest to narzędzie udostępniające alternatywny konstruktor do tworzenia
obiektów korzystających z parametrów przekazanych z linii poleceń.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--perl=%{__perl} \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Getopt.pm
%{perl_vendorlib}/MooseX/Getopt
%{_mandir}/man3/MooseX::Getopt*.3pm*
