%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	UUlib
Summary:	Convert::UUlib - Perl interface to the uulib library
Summary(pl):	Convert::UUlib - interfejs Perla dla biblioteki uulib
Name:		perl-Convert-UUlib
Version:	1.04
Release:	1
Epoch:		1
# same as perl, but library is GPL
License:	GPL
Vendor:		Marc Lehmann <pcg@goof.com>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ca72fd4343c30368be005bf60d5fb27
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UUlib Perl module is an interface to the uulib
decoding/encoding library (a.k.a uudeview/uuenview).

%description -l pl
Modu³ Perla Convert::UUlib stanowi interfejs Perla dla biblioteki
koduj±cej/rozkodowuj±cej uulib (nazywanej te¿ uudeview/uuenview).

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
