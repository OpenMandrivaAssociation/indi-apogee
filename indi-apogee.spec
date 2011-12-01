Summary: INDI driver for Apgoee Alta (U & E) line of CCDs
Name: indi-apogee
Version: 1.0
Release: %mkrel 5
Source0: http://downloads.sourceforge.net/indi/%{name}_%{version}.tar.gz
Patch0: indi-apogee_1.0-fix-str-fmt.patch
Patch1: indi-apogee_1.0-cfitsio-prefix.path
License: LGPLv2+
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://indi.sourceforge.net/
BuildRequires: zlib-devel
BuildRequires: libusb-devel
BuildRequires: cfitsio-devel
BuildRequires: indilib-devel
BuildRequires: libapogee-devel
BuildRequires: libnova-devel
BuildRequires: cmake

%description
This package provides the INDI driver for Apgoee Alta (U & E) line of CCDs.

%prep
%setup -q -n %name-%version
%patch0 -p0
%patch1 -p0

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%_bindir/indi_apogeee_ccd
%_bindir/indi_apogeeu_ccd
%_datadir/indi/indi_apogee.xml
