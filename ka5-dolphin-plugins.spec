%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		dolphin-plugins
Summary:	Dolphin plugins
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	dec62349124c2cf78661c8c165c166e6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dolphin plugins.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/fileviewbazaarplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fileviewdropboxplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fileviewgitplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fileviewhgplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fileviewsvnplugin.so
%{_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_datadir}/kservices5/fileviewbazaarplugin.desktop
%{_datadir}/kservices5/fileviewdropboxplugin.desktop
%{_datadir}/kservices5/fileviewgitplugin.desktop
%{_datadir}/kservices5/fileviewhgplugin.desktop
%{_datadir}/kservices5/fileviewsvnplugin.desktop
