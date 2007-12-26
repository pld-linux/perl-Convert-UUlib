%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	UUlib
Summary:	Convert::UUlib - Perl interface to the uulib library
Summary(pl.UTF-8):	Convert::UUlib - interfejs Perla dla biblioteki uulib
Name:		perl-Convert-UUlib
Version:	1.09
Release:	1
Epoch:		2
# same as perl, but library is GPL
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f4cfa860176f60a83b56816d5917e71a
URL:		http://search.cpan.org/dist/Convert-UUlib/
BuildRequires:	perl-devel >= 1:5.8.0
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Convert/UUlib/UUlib.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Convert/UUlib/UUlib.so
%{_mandir}/man3/*
