Summary: serene-sddm-chili
Name: serene-sddm-chili
Version: 1.0.0
Release: 1%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kahenteikou
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/sddm-chili/archive/23562d37ef2cbec0739b17bfadf7306d9886d295.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n sddm-chili-23562d37ef2cbec0739b17bfadf7306d9886d295

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/sddm/themes/sddm-chili
cp -arf . $RPM_BUILD_ROOT/usr/share/sddm/themes/sddm-chili/


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/share/sddm/themes/sddm-chili/
%changelog
