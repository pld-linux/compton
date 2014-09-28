%define		snap	20140928
#
Summary:	Compositor for X11
Name:		compton
Version:	0.0.1
Release:	0.%{snap}.1
License:	MIT
Group:		X11/Applications
Source0:	%{name}-%{snap}.tar.xz
# Source0-md5:	96f8d006045b8f4bcc318c9383364e9d
URL:		https://github.com/chjj/compton
BuildRequires:	OpenGL-devel
BuildRequires:	asciidoc
BuildRequires:	dbus-devel
BuildRequires:	libconfig-devel
BuildRequires:	libdrm-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compositor for X11.

%prep
%setup -q -n %{name}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
COMPTON_VERSION="%{snap}" \
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

PREFIX="%{_prefix}" \
MANDIR="%{_mandir}/man1" \
APPDIR="%{_desktopdir}" \
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md compton.sample.conf
%attr(755,root,root) %{_bindir}/compton
%attr(755,root,root) %{_bindir}/compton-trans
%{_desktopdir}/compton.desktop
%{_mandir}/man1/compton.1*
%{_mandir}/man1/compton-trans.1*
