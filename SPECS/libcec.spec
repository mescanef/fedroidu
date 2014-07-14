# Tarfile created using git
# git clone https://github.com/Pulse-Eight/libcec.git
# git archive --format=tar --prefix=%{name}-%{version}/ %{name}-%{version} | bzip2 > ~/%{name}-%{version}.tar.bz2

Name:          libcec
Version:       2.1.3.odroidu
Release:       2%{?dist}
Summary:       Library and utilities for HDMI-CEC device control

Group:         System Environment/Libraries
License:       GPLv2+
URL:           http://libcec.pulse-eight.com/
Source0:       %{name}-%{version}.tar.bz2

BuildRequires: systemd-devel lockdev-devel
BuildRequires: libtool autoconf automake

%description
libCEC allows you in combination with the right hardware to control your device 
with your TV remote control over your existing HDMI cabling.

libCEC is an enabling platform for the CEC bus in HDMI, it allows developers to 
interact with other HDMI devices without having to worry about the communication 
overhead, handshaking, and the various ways of send messages for each vendor.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q

# Remove non linux binaries
rm support/p8-usbcec-driver-installer.exe
rm -rf driver

%build
chmod +x bootstrap
./bootstrap
#autoreconf -vif
%configure \
--disable-static \
%ifarch armv7hl
--enable-exynos \
%endif

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README AUTHORS ChangeLog
%{_bindir}/cec-client
%{_libdir}/libcec.so.*

%files devel
%{_includedir}/libcec
%{_libdir}/pkgconfig/libcec.pc
%{_libdir}/libcec.so

%changelog
* Sun Jul 13 2014 mescanef <zone@mescanef.net> - 2.1.3.odroidu
- Prepare build for exynos, ARM based, boards (odroidu's)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.3-1
- Update to 2.1.3

* Mon Mar  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.5-1
- Update to 2.0.5

* Sun Nov 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.4-1
- Update to 2.0.4

* Mon Nov 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.3-1
- Update to 2.0.3

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-2
- Updates from review

* Wed Sep 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-1
- Update to 1.9.0

* Sat Jun 30 2012 Peter Robinson <pbrobinson@gmail.com> 1.7.1-1
- Initial packaging
