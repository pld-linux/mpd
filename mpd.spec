# TODO:
# - add initscript
# - create user for daemon (group audio)
# - add dir to store playlists and songs DB
# - create default config
# - add logrotate
Summary:	Music Player Daemon
Summary(pl.UTF-8):	Music Player Daemon - demon odtwarzający muzykę
Name:		mpd
Version:	0.13.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://musicpd.org/uploads/files/%{name}-%{version}.tar.bz2
# Source0-md5:	dbd219c8ba773bc9270e27bfafc798b5
URL:		http://www.musicpd.org/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	audiofile-devel >= 0.1.7
BuildRequires:	avahi-devel
BuildRequires:	faad2-devel
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.4
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel >= 3.1.7
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel >= 0.0.15
BuildRequires:	libshout-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists.
MPD is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It is also
makes a great desktop music player, especially if you are a console
junkie, like frontend options, or restart X often.

%description -l pl.UTF-8
Music Player Daemon (MPD) pozwala na zdalny dostęp do odtwarzania
muzyki (plików MP3, Ogg Vorbis, FLAC, AAC, Mod i wave) oraz
zarządzania playlistami. MPD jest zaprojektowany do integrowania
komputera w system stereo umożliwiający sterowanie odtwarzaniem muzyki
w sieci lokalnej. Służy także za dobry odtwarzacz muzyki dla
komputerów biurkowych, zwłaszcza dla miłośników konsoli, różnych opcji
frontendów albo często restartujących X.

%prep
%setup -q

%build
# ac_cv_* hacks to avoid unwanted linking
%configure \
	ac_cv_lib_iconv_main=no \
	ac_cv_lib_nsl_gethostbyname=no \
	--enable-ao
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/mpdconf.example UPGRADING doc/COMMANDS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
