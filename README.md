# Scoop bucket chính thức của tsudev

Cài các app/tool [tsudev](https://tsudev.com) trên Windows bằng [Scoop](https://scoop.sh) - không cần quyền quản trị.

```powershell
scoop bucket add tsudev https://github.com/tsudev-org/scoop-bucket
scoop install tsudev/tsudev-trafficmonitor
```

| Gói | Sản phẩm | Lệnh |
| --- | --- | --- |
| `tsudev-trafficmonitor` | [tsudev-trafficmonitor](https://trafficmonitor.tsudev.com) - tốc độ mạng, CPU, RAM trên thanh tác vụ (x64, x86, ARM64) | `scoop install tsudev/tsudev-trafficmonitor` |
| `tsudev-files` | [tsudev Files](https://files.tsudev.com) - chuyển đổi tệp ngoại tuyến 260+ định dạng (lệnh `tsudev-files`) | `scoop install tsudev/tsudev-files` |
| `tsudev-swico` | [SWICO](https://swico.tsudev.com) - kiểm tra bản quyền Windows/Office, cấu hình máy (lệnh `tsudev-swico`) | `scoop install tsudev/tsudev-swico` |
| `lotus-share` | [Lotus Share](https://lotus.tsudev.com) - gửi tệp trong mạng nội bộ, tương thích LocalSend (tên cũ `tsudev-lotus` vẫn cập nhật, nên chuyển) | `scoop install tsudev/lotus-share` |

Cập nhật: `scoop update *`. Gỡ: `scoop uninstall <gói>`.

## Danh mục máy đọc

[`catalog.json`](catalog.json) (schema 1, cùng dạng `https://pkg.tsudev.com/catalog.json`) liệt kê mọi gói trong
bucket: phiên bản, kiến trúc, lệnh, gói thay thế khi đổi tên (`replacedBy`), lệnh cài. Website `*.tsudev.com` và
`install.ps1` của tsudev.com đọc tệp này lúc build qua
`https://raw.githubusercontent.com/tsudev-org/scoop-bucket/main/catalog.json`. Sinh bằng `python3 tools/catalog.py`;
CI từ chối nếu tệp cũ, `excavator` sinh lại cùng commit cập nhật manifest.

## Bảo mật

- Mọi manifest ghim **SHA-256** của tệp tải về. Mã băm lấy từ `SHA256SUMS` của chính Release trên `tsudev-org`,
  không chép tay; Scoop từ chối cài nếu tệp không khớp.
- Workflow `excavator` kiểm Release mới mỗi 6 giờ, **cài thử thật** trên Windows trước khi cập nhật manifest.
- Quy ước đóng gói: [`tsudev-standards/docs/PACKAGING.md`](https://github.com/tsudev-org/tsudev-standards/blob/main/docs/PACKAGING.md).
- Báo lỗ hổng: theo `SECURITY.md` của repo sản phẩm tương ứng, không mở Issue công khai.
