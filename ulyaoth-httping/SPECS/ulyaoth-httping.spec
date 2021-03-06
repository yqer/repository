Summary:    Httping is like 'ping' but for http-requests.
Name:       ulyaoth-httping
Version:    2.5
Release:    1%{?dist}
BuildArch: x86_64
License:    GNUv2
Group:      Applications/System
URL:        https://www.vanheusden.com/httping/
Vendor:     vanheusden.com
Packager:   Sjir Bagmeijer <sjir.bagmeijer@ulyaoth.com>
Source0:    https://github.com/flok99/httping/archive/v%{version}.tar.gz
BuildRoot:  %{_tmppath}/httping-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: fftw3-devel

Requires: ncurses
Requires: openssl
Requires: fftw3

Provides: httping
Provides: ulyaoth-httping

%description
ttping is like 'ping' but for http-requests.
Give it an url, and it'll show you how long it takes to connect, send a request and retrieve the reply (only the headers). Be aware that the transmission across the network also takes time! So it measures the latency of the webserver + network.
It supports, of course, IPv6.

%prep
%setup -q -n httping-%{version}

%build
%if 0%{?rhel}  == 6
./configure --with-ncurses --with-openssl --with-fftw3
%else
./configure --with-tfo --with-ncurses --with-openssl --with-fftw3
%endif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
   
%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root)
%docdir /usr/share/doc/httping

%{_bindir}/httping
%{_mandir}/man1/httping.1.gz
%{_mandir}/nl/man1/httping-nl.1.gz
%{_mandir}/ru/man1/httping-ru.1.gz

%doc %{_datadir}/doc/httping/license.txt
%doc %{_datadir}/doc/httping/license.OpenSSL
%doc %{_datadir}/doc/httping/readme.txt
%{_datadir}/locale/nl/LC_MESSAGES/httping.mo
%{_datadir}/locale/ru/LC_MESSAGES/httping.mo

%post
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-httping!

Please find the official documentation for httping here:
* https://www.vanheusden.com/httping/

For any additional information or help regarding this rpm:
Website: https://ulyaoth.com
Forum: https://community.ulyaoth.com

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Sat Oct 15 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.5-1
- Updated to httping 2.5.

* Wed Jun 8 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 2.4-1
- Initial release.