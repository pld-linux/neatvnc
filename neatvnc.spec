#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Neat VNC server library
Summary(pl.UTF-8):	Neat VNC - schludna biblioteka serwera VNC
Name:		neatvnc
Version:	0.7.1
Release:	1
License:	ISC
Group:		Libraries
#https://github.com/any1/neatvnc/releases
Source0:	https://github.com/any1/neatvnc/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	230c9d236686d79d9f72e96c9842b70a
URL:		https://github.com/any1/neatvnc
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	aml-devel >= 0.3.0
BuildRequires:	aml-devel < 0.4
# libavcodec libavfilter libavutil
BuildRequires:	ffmpeg-devel
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gmp-devel
BuildRequires:	gnutls-devel
BuildRequires:	libdrm-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	meson
BuildRequires:	nettle-devel
BuildRequires:	ninja >= 1.5
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a liberally licensed VNC server library that's intended to be
fast and neat.

Goals:
- Speed
- Clean interface
- Interoperability with the Freedesktop.org ecosystem

%description -l pl.UTF-8
Biblioteka serwera VNC na liberalnej lincencji, tworzona z myślą o
szybkości i schludności.

Cele:
- szybkość
- czysty interfejs
- współpraca z ekosystemem Freedesktop.org

%package devel
Summary:	Header files for neatvnc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki neatvnc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Mesa-libgbm-devel
Requires:	aml-devel >= 0.3.0
Requires:	aml-devel < 0.4
# libavcodec libavfilter libavutil
Requires:	ffmpeg-devel
Requires:	gnutls-devel
Requires:	libdrm-devel
Requires:	libjpeg-turbo-devel
Requires:	pixman-devel
Requires:	zlib-devel

%description devel
Header files for neatvnc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki neatvnc.

%package static
Summary:	Static neatvnc library
Summary(pl.UTF-8):	Statyczna biblioteka neatvnc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static neatvnc library.

%description static -l pl.UTF-8
Statyczna biblioteka neatvnc.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libneatvnc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libneatvnc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libneatvnc.so
%{_includedir}/neatvnc.h
%{_pkgconfigdir}/neatvnc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libneatvnc.a
%endif
