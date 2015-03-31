Summary:	Embedding of arbitrary application windows into the Xfce panel.
Name:		xfce4-embed-plugin
Version:	1.4.1
Release:	1
License:	LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-embed-plugin/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	6d1021c0af861241d73971085cde5e52
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-embed-plugin
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin enables the embedding of arbitrary application windows
into the Xfce panel. The window is resized into the panel space
available, and the associated program can be automatically launched
if it is not open.

Example uses include embedding an instant messaging buddy list, a mail
client's new mail ticker, a simple media application, or a fancy clock
or timer. Combining with Xfce's ability to auto-hide panels can make
this very convenient.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libembed.so
%{_datadir}/xfce4/panel/plugins/embed.desktop
