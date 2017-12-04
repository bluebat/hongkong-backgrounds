VERSION = 201712
DESTDIR =
PREFIX = /usr
PACKAGE = hongkong-backgrounds

build:

install:
	install -d $(DESTDIR)$(PREFIX)/share/backgrounds/hongkong
	install -m644 *.jpg $(DESTDIR)$(PREFIX)/share/backgrounds/hongkong
	install -Dm644 $(PACKAGE).xml $(DESTDIR)$(PREFIX)/share/gnome-background-properties/$(PACKAGE).xml
	install -Dm644 $(PACKAGE).xml $(DESTDIR)$(PREFIX)/share/mate-background-properties/$(PACKAGE).xml

uninstall:
	rm -rf $(DESTDIR)$(PREFIX)/share/backgrounds/hongkong
	rm -f $(DESTDIR)$(PREFIX)/share/gnome-background-properties/${PACKAGE).xml
	rm -f $(DESTDIR)$(PREFIX)/share/mate-background-properties/$(PACKAGE).xml

clean:

rpm: $(PACKAGE).spec
	rsync -aC --delete . $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION)
	tar czf $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION).tar.gz -C $(HOME)/rpmbuild/SOURCES $(PACKAGE)-$(VERSION)
	rpmbuild -ta $(HOME)/rpmbuild/SOURCES/$(PACKAGE)-$(VERSION).tar.gz
