
Summary:    s3fs allows Linux and Mac OS X to mount an S3 bucket via FUSE.
Name:       ulyaoth-fuse-s3fs
Version:    1.79
Release:    1%{?dist}
BuildArch: x86_64
License:    GNUv2
Group:      Applications/System
URL:        https://github.com/s3fs-fuse/s3fs-fuse
Vendor:     Randy Rizun
Packager:   Sjir Bagmeijer <sbagmeijer@ulyaoth.net>
Source0:    https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}.tar.gz
BuildRoot:  %{_tmppath}/s3fs-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc
BuildRequires: libstdc++-devel
BuildRequires: gcc-c++
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: mailcap
BuildRequires: automake
BuildRequires: libcurl-devel
BuildRequires: git
BuildRequires: make
BuildRequires: ulyaoth-fuse

Requires: curl
Requires: openssl
Requires: mailcap
Requires: libxml2
Requires: libstdc++
Requires: ulyaoth-fuse

Provides: fuse-s3fs
Provides: ulyaoth-fuse-s3fs

%description
s3fs allows Linux and Mac OS X to mount an S3 bucket via FUSE. s3fs preserves the native object format for files, allowing use of other tools like s3cmd.

%prep
%setup -q -n s3fs-fuse-%{version}

%build
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
   
%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root)
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1.gz

%post
cat <<BANNER
----------------------------------------------------------------------

Thanks for using ulyaoth-fuse-s3fs!

Please find the official documentation for fuse-s3fs here:
* https://github.com/s3fs-fuse/s3fs-fuse

For any additional help please visit my forum at:
* https://www.ulyaoth.net

----------------------------------------------------------------------
BANNER

%preun

%postun

%changelog
* Sun Apr 10 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.79-1
- Initial release.