# TODO:
# - add initscript
# - create user for daemon (group audio)
# - add dir to store playlists and songs DB
# - create default config 
# - add logrotate
Summary:	Music Player Daemon
Name:		mpd
Version:	0.11.5
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Multimedia
Source0:	http://mercury.chem.pitt.edu/~shank/%{name}-%{version}.tar.gz
# Source0-md5:	1a9a1a9d31f00a43838b3752024f7ebe
URL:		http://www.musicpd.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel >= 0.1.7
BuildRequires:	faad2-devel
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
#BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpd

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO UPGRADING doc/COMMANDS doc/mpdconf.example

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/mpd.1*

#%{_datadir}/%{name}

# initscript and it's config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
