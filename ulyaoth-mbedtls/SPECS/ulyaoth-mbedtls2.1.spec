%define debug_package %{nil}

# distribution specific definitions

%if 0%{?fedora} >= 18
BuildRequires: pkcs11-helper-devel
%endif

# end of distribution specific definitions

Summary: mbed TLS is an open source and commercial SSL library licensed by ARM Limited.. mbed TLS used to be called PolarSSL,
Name: ulyaoth-mbedtls2.1
Version: 2.1.9
Release: 1%{?dist}
BuildArch: x86_64
Vendor: ARM Limited.
URL: https://tls.mbed.org/
Packager: Sjir Bagmeijer <sjir.bagmeijer@ulyaoth.com>

Source0: https://github.com/ARMmbed/mbedtls/archive/mbedtls-%{version}.tar.gz

License: GPLv2 or proprietary

BuildRoot: %{_tmppath}/mbedtls-%{version}-%{release}-root
BuildRequires: ulyaoth-cmake
BuildRequires: zlib-devel
BuildRequires: openssl-devel

Provides: mbedtls
Provides: ulyaoth-mbedtls2.1

Conflicts: ulyaoth-mbedtls
Conflicts: ulyaoth-mbedtls2.2
Conflicts: ulyaoth-mbedtls2.3
Conflicts: ulyaoth-mbedtls2.4
Conflicts: ulyaoth-mbedtls2.5
Conflicts: ulyaoth-mbedtls2.6

%description
mbed TLS (formerly known as PolarSSL) makes it trivially easy for developers to include cryptographic and SSL/TLS capabilities in their (embedded) products, facilitating this functionality with a minimal coding footprint.

%prep
%setup -q -n mbedtls-mbedtls-%{version}
sed -i 's|//\(#define MBEDTLS_THREADING_C\)|\1|' include/mbedtls/config.h
sed -i 's|//\(#define MBEDTLS_THREADING_PTHREAD\)|\1|' include/mbedtls/config.h

%build
%if 0%{?fedora} >= 18
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_BUILD_TYPE:String="Release" -DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE -DENABLE_ZLIB_SUPPORT:BOOL=TRUE -DUSE_PKCS11_HELPER_LIBRARY:BOOL=TRUE .
%else
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_BUILD_TYPE:String="Release" -DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE -DENABLE_ZLIB_SUPPORT:BOOL=TRUE .
%endif
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libexecdir}/mbedtls

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_libexecdir}/mbedtls/*
%{_includedir}/mbedtls/*
/usr/lib/*
%dir %{_includedir}/mbedtls

%pre

%post
# print site info
    cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-mbedtls2.1!

Please find the official documentation for mbedtls here:
* https://tls.mbed.org

For any additional information or help regarding this rpm:
Website: https://ulyaoth.com
Forum: https://community.ulyaoth.com

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Thu Nov 16 2017 Sjir Bagmeijer <sjir.bagmeijer@ulyaoth.net> 2.1.9-1
- Updated to mbed TLS 2.1.9.
- Added conflict for mbed TLS 2.6.

* Sat Jul 1 2017 Sjir Bagmeijer <sjir.bagmeijer@ulyaoth.net> 2.1.8-1
- Updated to mbed TLS 2.1.8.
- Added conflict for mbed TLS 2.5.

* Fri Mar 17 2017 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.7-1
- Updated to mbed TLS 2.1.7.

* Sat Oct 22 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.6-1
- Updated to mbed TLS 2.1.6.

* Sat Jul 2 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.5-1
- Updated to mbed TLS 2.1.5.

* Mon Jan 11 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.4-2
- Removed obsoletes due to problems.

* Fri Jan 8 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.4-1
- Updated to mbed TLS 2.1.4.

* Sat Nov 14 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.3-1
- Updated to version 2.1.3.

* Sun Oct 18 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.2-1
- Initial release for version 2.1.2.

* Sun Sep 20 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.1-1
- Initial release for version 2.1.1.

* Sat Sep 5 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.1.0-1
- Initial release for version 2.1.0.

* Thu Aug 20 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.0.0-3
- Added obsoletes and conflicts package ulyaoth-mbedtls.

* Fri Aug 14 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.0.0-2
- Recompiled with the github fixes for libmbedcrypto.a and libmbedx509.a.

* Tue Jul 28 2015 Sjir Bagmeijer <sbagmeijer@ulyaoth.co.kr> 2.0.0-1
- Initial release for version 2.0.0.
