Summary:	INDI driver for Apgoee Alta (U & E) line of CCDs
Name:		indi-apogee
Version:	1.0
Release:	6
License:	LGPLv2+
Group:		Development/Other
Url:		http://indi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/indi/%{name}_%{version}.tar.gz
Patch0:		indi-apogee_1.0-fix-str-fmt.patch
Patch1:		indi-apogee_1.0-cfitsio-prefix.path
Patch2:		indi-apogee_1.0-dso.patch
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(libindi)
BuildRequires:	indi-devel-static
BuildRequires:	libapogee-devel
BuildRequires:	libnova-devel
BuildRequires:	cmake

%description
This package provides the INDI driver for Apgoee Alta (U & E) line of CCDs.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc ChangeLog README
%{_bindir}/indi_apogeee_ccd
%{_bindir}/indi_apogeeu_ccd
%{_datadir}/indi/indi_apogee.xml
