%define lib_major 2
%define api_version 2
%define lib_name %mklibname %{name} %{api_version} %{lib_major}

%define req_gail_version 0.17
%define req_libglade_version 2.0.0
%define req_gnome_menus_version 2.13

Name:		eel
Summary:	Eazel Extensions Library
Version:	2.19.4
Release:	%mkrel 1
License: 	LGPL/GPL
Group:		System/Libraries
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) 2.10.1-3mdk fix load of KDE icons
Patch1:		eel-2.10.1-kdeicons.patch

URL: 		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gnome-desktop-devel
BuildRequires:	libgail-devel >= %{req_gail_version}
BuildRequires:	libglade2.0-devel >= %{req_libglade_version}
BuildRequires:	gnome-menus-devel >= %{req_gnome_menus_version}
BuildRequires:	perl-XML-Parser expat-devel

%description
Eazel Extensions Library

%package -n	%{lib_name}
Summary:	Eazel Extensions shared Libraries
Group:		%{group}
Requires:	%{name} >= %{version}-%{release}

%description -n	%{lib_name}
Eazel Extensions shared libraries

%package -n	%{lib_name}-devel
Summary:	Libraries and include files for developing with Eel
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	lib%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel

%description -n	%{lib_name}-devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.


%prep
%setup -q
%patch1 -p1 -b .kdeicons

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

%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{name}-2.0.lang
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB NEWS README

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/*.so.*


%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc ChangeLog
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/eel-%{api_version}


