%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		dolphin-plugins
Summary:	Dolphin plugins
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cda075981571d51e0c20607f58c84fe4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-ki18n-devel >= 5.0.0
BuildRequires:	kf5-kio-devel >= 5.0.0
BuildRequires:	kf5-ktexteditor-devel >= 5.0.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.0.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.0.0
BuildRequires:	kf5-kxmlgui-devel >= 5.0.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Dolphin.

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
