%define lib_major 2
%define api_version 2
%define libname %mklibname %{name} %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{name} %{api_version}

%define req_gail_version 0.17
%define req_libglade_version 2.0.0
%define req_gnomedesktop_version 2.23.3

Name:		eel
Summary:	Eazel Extensions Library
Version:	2.23.91
Release:	%mkrel 1
License: 	LGPLv2+
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2

URL: 		http://www.gnome.org/
BuildRequires:	gnome-desktop-devel >= %{req_gnomedesktop_version}
BuildRequires:	libgail-devel >= %{req_gail_version}
BuildRequires:	libglade2.0-devel >= %{req_libglade_version}
BuildRequires:	libgnome2-devel >= 2.23.0
BuildRequires:	glib2-devel >= 2.15.2
BuildRequires:	perl-XML-Parser expat-devel
BuildRequires:  intltool

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

%build

%configure2_5x

%make LIBS=-lm

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%{find_lang} %{name}-2.0
rm -f %_libdir/debug%_libdir/?

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

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


