%define		kdeappsver	21.12.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		dolphin-plugins
Summary:	Dolphin plugins
Name:		ka5-%{kaname}
Version:	21.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fceb64759bd8d06f95de79caea806425
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Dolphin.

%description -l pl.UTF-8
Wtyczki do Dolphina.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kfileitemaction/mountisoaction.so
%{_datadir}/metainfo/org.kde.dolphin-plugins.metainfo.xml
%dir %{_libdir}/qt5/plugins/dolphin/vcs
%{_libdir}/qt5/plugins/dolphin/vcs/fileviewbazaarplugin.so
%{_libdir}/qt5/plugins/dolphin/vcs/fileviewdropboxplugin.so
%{_libdir}/qt5/plugins/dolphin/vcs/fileviewgitplugin.so
%{_libdir}/qt5/plugins/dolphin/vcs/fileviewhgplugin.so
%{_libdir}/qt5/plugins/dolphin/vcs/fileviewsvnplugin.so
