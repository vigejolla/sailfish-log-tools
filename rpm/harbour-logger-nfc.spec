Name:       harbour-logger-nfc
Summary:    NFC logger
Version:    1.0.21
Release:    1
Group:      Applications/System
License:    BSD
URL:        http://github.com/monich/harbour-logger
Source0:    %{name}-%{version}.tar.bz2

Requires:   sailfishsilica-qt5
BuildRequires: pkgconfig(sailfishapp)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(mlite5)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: desktop-file-utils
BuildRequires: qt5-qttools-linguist

%description
Application for gathering NFC logs on Sailfish OS

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake5
%qtc_make %{?_smp_mflags} logger-nfc

%install
rm -rf %{buildroot}
%qmake5_install -C nfc

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%global privileges_dir %{_datarootdir}/mapplauncherd/privileges.d
%dir %{privileges_dir}
%{_bindir}/%{name}
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/translations
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{privileges_dir}/%{name}

%changelog
* Wed Dec 01 2021 Slava Monich <slava.monich@jolla.com> 1.0.21
- Restore log level on exit
- Fixed cover log and allow cover scaling

* Sat Sep 18 2021 Slava Monich <slava.monich@jolla.com> 1.0.20
- Copy log entry to clipboard on long tap
- Improved sandbox behavior

* Fri Sep 17 2021 Slava Monich <slava.monich@jolla.com> 1.0.19
- Complain about not being privileged
- Tweaked settings page

* Mon Jul 19 2021 Slava Monich <slava.monich@jolla.com> 1.0.18
- Updated Polish translation

* Sun Jul 18 2021 Slava Monich <slava.monich@jolla.com> 1.0.17
- Disable broken in-app sharing
- Added Polish translation

* Sat Dec 12 2020 Slava Monich <slava.monich@jolla.com> 1.0.16
- Show page header when scrolling
- Added "Jump to bottom" button
- Fixed email sharing with latest Sailfish OS
- Fixed build of translations with newer Qt

* Sat Dec 14 2019 Slava Monich <slava.monich@jolla.com> 1.0.15
- Fixed settings icon name
- Updated list of NFC related packages
- Updated submodules

* Sun Mar 10 2019 Slava Monich <slava.monich@jolla.com> 1.0.14
- Dump versions of plugins and related libraries

* Sat Mar 9 2019 Slava Monich <slava.monich@jolla.com> 1.0.13
- Added NFC logger
