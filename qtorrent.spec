Summary:	A PyQt GUI for BitTorrent
Summary(pl.UTF-8):	Interfejs GUI do BitTorrenta
Name:		qtorrent
Version:	0.9.6.1
Release:	2
License:	MIT
Group:		Applications/Networking
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ee6164fb26e0400f6083516f59ea77a3
URL:		http://thegraveyard.org/qtorrent.php
BuildRequires:	python
BuildRequires:	python-PyQt
BuildRequires:	python-devel
BuildRequires:	python-modules
%pyrequires_eq	python-libs
Requires:	python-PyQt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QTorrent is a BitTorrent client that uses the Qt widget-set. It allows
you to have several torrents open at the same time from within the
same program window, offering you easy overview, access and management
through a list-mode. Every torrent also has it's own page where you
can control things like upload speed and upload slots. A page that
shows some statistics of all open torrents is also available.

%description -l pl.UTF-8
QTorrent jest klientem BitTorrenta używającym widgetów Qt. Pozwala na
otwarcie kilku torrentów jednocześnie w jednym oknie programu. Oferuje
łatwy podgląd, dostęp i zarządzanie przez listę. Każdy potok
("torrent") ma także własną stronę przez która można kontrolować
szybkość uploadu i sloty. Strona też przedstawia pewne statystyki
wszystkich otwartych potoków.

%prep
%setup -q

%build
%{__python} setup.py build

# regenerate from ui files
cd pyqtorrent
pyuic torrentwidget.ui > torrentwidget.py
pyuic torrentwindow.ui > torrentwindow.py
pyuic torrentsettings.ui > torrentsettings.py

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt MANIFEST PKG-INFO
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/pyqtorrent
%dir %{py_sitescriptdir}/pyqtorrent/BitTornado
%dir %{py_sitescriptdir}/pyqtorrent/BitTornado/BT1
%{py_sitescriptdir}/pyqtorrent/*.py[co]
%{py_sitescriptdir}/pyqtorrent/BitTornado/*.py[co]
%{py_sitescriptdir}/pyqtorrent/BitTornado/BT1/*.py[co]
