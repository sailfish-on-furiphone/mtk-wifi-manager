Name:       mtk-wifi-manager
Summary:    WiFi manager for MediaTek WMT driver
Version:    1.1.0
Release:    1
License:    LICENSE
URL:        https://gitlab.com/mobian1/devices/eg25-manager
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: libhybris-devel
BuildRequires: glib2-devel
BuildRequires: libnl-devel

%description
WiFi manager for MediaTek WMT driver

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
make

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/multi-user.target.wants
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/multi-user.target.wants/%{name}.service

%preun
if [ "$1" -eq 0 ]; then
systemctl stop %{name}.service || :
fi

%post
/sbin/ldconfig
systemctl daemon-reload || :
systemctl reload-or-try-restart %{name}.service || :

%postun
/sbin/ldconfig
systemctl daemon-reload || :

%files
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/multi-user.target.wants/%{name}.service
%{_datadir}/dbus-1/system-services/com.MediaTek.WiFiManager.service
%{_datadir}/dbus-1/system.d/com.MediaTek.WiFiManager.conf
