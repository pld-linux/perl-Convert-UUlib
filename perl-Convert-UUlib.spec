%define		pdir	Convert
%define		pnam	UUlib
Summary:	Convert::UUlib - Perl interface to the uulib library
Summary(pl.UTF-8):	Convert::UUlib - interfejs Perla dla biblioteki uulib
Name:		perl-Convert-UUlib
Version:	1.71
Release:	1
Epoch:		2
# same as perl, but library is GPL
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da734f09c9a73aed957d6dd5034bd856
URL:		http://search.cpan.org/dist/Convert-UUlib/
BuildRequires:	perl-Canary-Stability >= 2012
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UUlib Perl module is an interface to the uulib
decoding/encoding library (a.k.a uudeview/uuenview).

%description -l pl.UTF-8
Moduł Perla Convert::UUlib stanowi interfejs Perla dla biblioteki
kodującej/rozkodowującej uulib (nazywanej też uudeview/uuenview).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
PERL_CANARY_STABILITY_NOPROMPT=1 \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README example-decoder
%{perl_vendorarch}/Convert/*
%dir %{perl_vendorarch}/auto/Convert/UUlib
%attr(755,root,root) %{perl_vendorarch}/auto/Convert/UUlib/UUlib.so
%{_mandir}/man3/*
