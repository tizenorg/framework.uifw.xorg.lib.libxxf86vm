Summary: X.Org X11 libXxf86vm runtime library
Name: libXxf86vm
Version: 1.1.2
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xext) pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary: X.Org X11 libXxf86vm development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxxf86vm-devel

%description devel
X.Org X11 libXxf86vm development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc README COPYING ChangeLog
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
#%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/xf86vmode.h
