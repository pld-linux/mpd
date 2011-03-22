# TODO:
# - add logrotate
#
# Conditional build:
%bcond_without	mod		# enable MOD support
%bcond_without	pulseaudio	# disable PulseAudio support
#
Summary:	Music Player Daemon
Summary(hu.UTF-8):	Music Player Daemon
Summary(pl.UTF-8):	Music Player Daemon - demon odtwarzający muzykę
Name:		mpd
Version:	0.16.2
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2
# Source0-md5:	dedb75cef8e489f3de5231031876fb77
Source1:	%{name}.conf
Source2:	%{name}.init
URL:		http://www.musicpd.org/
BuildRequires:	OpenAL-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	audiofile-devel >= 0.1.7
BuildRequires:	avahi-glib-devel
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	faad2-devel >= 2.6.1-5
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	fluidsynth-devel
BuildRequires:	glib2-devel >= 2.12
BuildRequires:	jack-audio-connection-kit-devel >= 0.4
BuildRequires:	lame-libs-devel
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libcdio-devel
BuildRequires:	libcue-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
%{?with_mod:BuildRequires:	libmikmod-devel >= 3.1.7}
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel >= 0.0.15
BuildRequires:	libshout-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig >= 1:0.9.0
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
BuildRequires:	sqlite3-devel
BuildRequires:	twolame-devel
BuildRequires:	wavpack-devel
BuildRequires:	wildmidi-devel
BuildRequires:	xmlto
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel
Provides:	group(mpd)
Provides:	user(mpd)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists.
MPD is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It is also
makes a great desktop music player, especially if you are a console
junkie, like frontend options, or restart X often.

%description -l hu.UTF-8
Music Player Daemon (MPD)-vel lehetővé válik távoli zenelejátszás
(MP3, Ogg Vorbis, FLAC, AAC, Mod és wav fájlok) és lejátszási listák
menedzselése. Az MPD a számítógépben egy zenelejátszó, amelyet
irányíthatsz helyi hálózaton keresztül. Egyben egy zseniális desktop
zenelejátszó is, különösen a konzol-mániásoknak, vagy azoknak, akik
sűrűn indítják újra az X-et.

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
	%{!?with_pulseaudio:--disable-pulse} \
	%{?with_mod:--enable-mikmod} \
	--disable-sidplay \
	--enable-alsa \
	--enable-ao \
	--enable-audiofile \
	--enable-bzip2 \
	--enable-cue \
	--enable-curl \
	--enable-documentation \
	--enable-ffmpeg \
	--enable-fluidsynth \
	--enable-httpd-output \
	--enable-iso9660 \
	--enable-jack \
	--enable-lame-encoder \
	--enable-lastfm \
	--enable-lsr \
	--enable-mad \
	--enable-mms \
	--enable-modplug \
	--enable-mvp \
	--enable-openal \
	--enable-pipe-output \
	--enable-recorder-output \
	--enable-shout \
	--enable-sqlite \
	--enable-twolame-encoder \
	--enable-vorbis-encoder \
	--enable-wave-encoder \
	--enable-wavpack \
	--enable-wildmidi \
	--enable-zzip \
	--with-zeroconf=avahi \
	--without-tremor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{/var/lib/mpd/playlists,/var/log/mpd,/var/run/mpd}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mpd

touch $RPM_BUILD_ROOT/var/lib/mpd/mpd.db
touch $RPM_BUILD_ROOT/var/lib/mpd/mpdstate
touch $RPM_BUILD_ROOT/var/lib/mpd/sticker.sql
touch $RPM_BUILD_ROOT/var/log/mpd/mpd.log

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mpd

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 204 mpd
%useradd -u 204 -r -d /home/services/mpd -s /bin/false -c "Music Player Daemon (MPD) user" -g audio -G mpd mpd

%post
for f in mpd.log; do
	if [ ! -f /var/log/%{name}/$f ]; then
		touch /var/log/%{name}/$f
		chown mpd:mpd /var/log/%{name}/$f
		chmod 644 /var/log/%{name}/$f
	fi
done
/sbin/chkconfig --add mpd

%preun
if [ "$1" = "0" ]; then
	%service mpd stop
	/sbin/chkconfig --del mpd
fi

%postun
if [ "$1" = "0" ]; then
	%userremove mpd
	%groupremove mpd
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README doc/mpdconf.example UPGRADING doc/api doc/developer doc/protocol doc/user
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpd.conf
%attr(754,root,root) /etc/rc.d/init.d/mpd
%dir %attr(770,root,mpd) /var/lib/%{name}
%dir %attr(770,root,mpd) /var/lib/%{name}/playlists
%dir %attr(751,root,root) /var/log/%{name}
%dir %attr(770,root,mpd) /var/run/%{name}
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/mpd.db
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/mpdstate
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/sticker.sql
%attr(644,mpd,mpd) %ghost /var/log/%{name}/mpd.log
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*
