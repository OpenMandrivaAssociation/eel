%define lib_major 2
%define api_version 2
%define libname %mklibname %{name} %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{name} %{api_version}

%define req_gail_version 0.17
%define req_libglade_version 2.0.0
%define req_gnome_menus_version 2.13
%define req_gnomedesktop_version 2.21.4

Name:		eel
Summary:	Eazel Extensions Library
Version:	2.20.0
Release:	%mkrel 2
License: 	LGPL/GPL
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) 2.10.1-3mdk fix load of KDE icons
Patch1:		eel-2.10.1-kdeicons.patch
# (fc) 2.20.0-2mdv add support for new gnome-bg code (Fedora)
Patch2:		eel2-2.18.0.1-gnome-bg.patch

URL: 		http://www.gnome.org/
BuildRequires:	gnome-desktop-devel >= %{req_gnomedesktop_version}
BuildRequires:	libgail-devel >= %{req_gail_version}
BuildRequires:	libglade2.0-devel >= %{req_libglade_version}
BuildRequires:	gnome-menus-devel >= %{req_gnome_menus_version}
BuildRequires:	perl-XML-Parser expat-devel

%description
Eazel Extensions Library

%package -n	%{libname}
Summary:	Eazel Extensions shared Libraries
Group:		%{group}
Requires:	%{name} >= %{version}-%{release}

%description -n	%{libname}
Eazel Extensions shared libraries

%package -n	%{libnamedev}
Summary:	Libraries and include files for developing with Eel
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel
Obsoletes: %mklibname -d %{name} 2 2

%description -n	%{libnamedev}
This package provides the necessary development libraries and include
files to allow you to develop with Eel.


%prep
%setup -q
%patch1 -p1 -b .kdeicons
%patch2 -p1 -b .gnome-bg

%build

%configure2_5x

%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%{find_lang} %{name}-2.0
rm -f %_libdir/debug%_libdir/?

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{libname}

%postun -p /sbin/ldconfig -n %{libname}

%files -f %{name}-2.0.lang
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB NEWS README

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/libeel-%{api_version}.so.%{lib_major}*


%files -n %{libnamedev}
%defattr(-, root, root)
%doc ChangeLog
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/eel-%{api_version}


