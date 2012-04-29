
Name:       libxxf86vm
Summary:    X.Org X11 libXxf86vm runtime library
Version:    1.1.1
Release:    2.5
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86vidmodeproto) >= 2.2.99.1
BuildRequires:  pkgconfig(xorg-macros)


%description
Extension library for the XFree86-VidMode X extension.



%package devel
Summary:    X.Org X11 libXxf86vm development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
Extension development library for the XFree86-VidMode X extension



%prep
%setup -q -n %{name}-%{version}


%build
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# FIXME: missing some of these files %doc AUTHORS COPYING README INSTALL ChangeLog
%doc COPYING ChangeLog
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_includedir}/X11/extensions/xf86vmode.h
%doc %{_mandir}/man3/*.3*

