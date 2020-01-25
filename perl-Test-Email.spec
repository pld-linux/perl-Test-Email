#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%define		pdir	Test
%define		pnam	Email
Summary:	Test::Email Perl module - Test Email Contents
Name:		perl-Test-Email
Version:	0.07
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JAMES/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be2f80d2dbdd2f9c3329237402ebcf14
URL:		http://search.cpan.org/dist/Test-Email/
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Mail-Sendmail
BuildRequires:	perl-devel >= 1:5.8.7
%if %{with tests}
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Email Perl - Test Email Contents.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Email.pm
%{perl_vendorlib}/Test/POP3.pm
%{_mandir}/man3/*
