# TODO:
# - add initscript
# - create user for daemon (group audio)
# - add dir to store playlists and songs DB
# - create default config 
# - add logrotate
Summary:	Music Player Daemon
Summary(pl):	Music Player Daemon - demon odtwarzaj±cy muzykê
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
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists.
MPD is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It is also
makes a great desktop music player, especially if you are a console
junkie, like frontend options, or restart X often.

%description -l pl
Music Player Daemon (MPD) pozwala na zdalny dostêp do odtwarzania
muzyki (plików MP3, Ogg Vorbis, FLAC, AAC, Mod i wave) oraz
zarz±dzania playlistami. MPD jest zaprojektowany do integrowania
komputera w system stereo umo¿liwiaj±cy sterowanie odtwarzaniem muzyki
w sieci lokalnej. S³u¿y tak¿e za dobry odtwarzacz muzyki dla
komputerów biurkowych, zw³aszcza dla mi³o¶ników konsoli, ró¿nych opcji
frontendów albo czêsto restartuj±cych X.

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
