%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	UUlib
Summary:	Convert::UUlib Perl module
Summary(cs):	Modul Convert::UUlib pro Perl
Summary(da):	Perlmodul Convert::UUlib
Summary(de):	Convert::UUlib Perl Modul
Summary(es):	Módulo de Perl Convert::UUlib
Summary(fr):	Module Perl Convert::UUlib
Summary(it):	Modulo di Perl Convert::UUlib
Summary(ja):	Convert::UUlib Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Convert::UUlib ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Convert::UUlib
Summary(pl):	Modu³ Perla Convert::UUlib
Summary(pt):	Módulo de Perl Convert::UUlib
Summary(pt_BR):	Módulo Perl Convert::UUlib
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Convert::UUlib
Summary(sv):	Convert::UUlib Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Convert::UUlib
Summary(zh_CN):	Convert::UUlib Perl Ä£¿é
Name:		perl-Convert-UUlib
Version:	0.213
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UUlib - Perl interface to the uulib library.

%description -l pl
Convert::UUlib - interfejs Perla dla biblioteki uulib.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README example-decoder
%{perl_sitearch}/Convert
%dir %{perl_sitearch}/auto/Convert
%dir %{perl_sitearch}/auto/Convert/UUlib
%{perl_sitearch}/auto/Convert/UUlib/UUlib.bs
%{perl_sitearch}/auto/Convert/UUlib/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Convert/UUlib/UUlib.so
%{_mandir}/man3/*
