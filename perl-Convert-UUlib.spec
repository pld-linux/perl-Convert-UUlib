%include	/usr/lib/rpm/macros.perl
Summary:	Convert-UUlib perl module
Summary(pl):	Modu� perla Convert-UUlib
Name:		perl-Convert-UUlib
Version:	0.201
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-UUlib-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-UUlib - Perl interface to the uulib library.

%description -l pl
Convert-UUlib - interfjes perla dla biblioteki uulib.

%prep
%setup -q -n Convert-UUlib-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example-decoder
%{perl_sitearch}/Convert/UUlib.pm
%dir %{perl_sitearch}/auto/Convert/UUlib
%{perl_sitearch}/auto/Convert/UUlib/UUlib.bs
%{perl_sitearch}/auto/Convert/UUlib/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Convert/UUlib/UUlib.so
%{_mandir}/man3/*
