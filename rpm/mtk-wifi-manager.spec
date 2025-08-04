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
%autosetup -p1 -n %{name}-%{version}/upstram

%build
%make

%install
%make_install

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
