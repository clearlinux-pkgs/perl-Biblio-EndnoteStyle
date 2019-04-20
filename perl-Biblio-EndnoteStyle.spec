#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Biblio-EndnoteStyle
Version  : 0.06
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIRK/Biblio-EndnoteStyle-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIRK/Biblio-EndnoteStyle-0.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libb/libbiblio-endnotestyle-perl/libbiblio-endnotestyle-perl_0.06-1.debian.tar.xz
Summary  : 'reference formatting using Endnote-like templates'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Biblio-EndnoteStyle-bin = %{version}-%{release}
Requires: perl-Biblio-EndnoteStyle-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Biblio::EndnoteStyle
====================
This module provides a class that can format references according to
style templates resembling those used by Endnote.  For details, see
the POD documentation in lib/Biblio/EndnoteStyle.pm -- for example,
use:
$ perldoc lib/Biblio/EndnoteStyle.pm

%package bin
Summary: bin components for the perl-Biblio-EndnoteStyle package.
Group: Binaries
Requires: perl-Biblio-EndnoteStyle-license = %{version}-%{release}

%description bin
bin components for the perl-Biblio-EndnoteStyle package.


%package dev
Summary: dev components for the perl-Biblio-EndnoteStyle package.
Group: Development
Requires: perl-Biblio-EndnoteStyle-bin = %{version}-%{release}
Provides: perl-Biblio-EndnoteStyle-devel = %{version}-%{release}

%description dev
dev components for the perl-Biblio-EndnoteStyle package.


%package license
Summary: license components for the perl-Biblio-EndnoteStyle package.
Group: Default

%description license
license components for the perl-Biblio-EndnoteStyle package.


%prep
%setup -q -n Biblio-EndnoteStyle-0.06
cd ..
%setup -q -T -D -n Biblio-EndnoteStyle-0.06 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Biblio-EndnoteStyle-0.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Biblio-EndnoteStyle
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Biblio-EndnoteStyle/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Biblio/EndnoteStyle.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/endnote-format

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Biblio::EndnoteStyle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Biblio-EndnoteStyle/deblicense_copyright
