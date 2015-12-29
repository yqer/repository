buildarch="$(uname -m)"

useradd ulyaoth
cd /home/ulyaoth
su ulyaoth -c "rpmdev-setuptree"
cd /home/ulyaoth/rpmbuild/SPECS/
su ulyaoth -c "wget https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-tomcat-multi/SPECS/ulyaoth-tomcat-multi.spec"

if [ "$arch" != "x86_64" ]
then
sed -i '/BuildArch: x86_64/c\BuildArch: '"$buildarch"'' ulyaoth-tomcat-multi.spec
fi

if grep -q -i "release 22" /etc/fedora-release
then
dnf builddep -y ulyaoth-tomcat-multi.spec
elif grep -q -i "release 23" /etc/fedora-release
then
dnf builddep -y ulyaoth-tomcat-multi.spec
else
yum-builddep -y ulyaoth-tomcat-multi.spec
fi

su ulyaoth -c "spectool ulyaoth-tomcat-multi.spec -g -R"
su ulyaoth -c "rpmbuild -ba ulyaoth-tomcat-multi.spec"
cp /home/ulyaoth/rpmbuild/SRPMS/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/x86_64/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/i686/* /root/
cp /home/ulyaoth/rpmbuild/RPMS/i386/* /root/
su ulyaoth -c "rm -rf /home/ulyaoth/rpmbuild"
rm -rf /root/build-ulyaoth-tomcat-multi.sh