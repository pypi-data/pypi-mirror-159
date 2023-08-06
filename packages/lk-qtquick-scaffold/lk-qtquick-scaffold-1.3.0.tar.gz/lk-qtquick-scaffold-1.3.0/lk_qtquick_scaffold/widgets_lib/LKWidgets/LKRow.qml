import QtQuick

Row {
    height: pysize.row_height_m
    spacing: pysize.h_spacing_m

    property bool autoSize: false
    property bool centerAlignChildren: true

    Component.onCompleted: {
        if (this.centerAlignChildren) {
            for (let i = 0; i < this.children.length; i++) {
                this.children[i].anchors.verticalCenter = Qt.binding(() => {
                    return this.verticalCenter
                })
            }
        }
        if (this.autoSize) {
            pylayout.auto_size_children(this, pylayout.HORIZONTAL)
        }
    }
}
