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
| `tsudev-lotus` | [Lotus](https://lotus.tsudev.com) - gửi tệp trong mạng nội bộ | `scoop install tsudev/tsudev-lotus` |

Cập nhật: `scoop update *`. Gỡ: `scoop uninstall <gói>`.

## Bảo mật

- Mọi manifest ghim **SHA-256** của tệp tải về. Mã băm lấy từ `SHA256SUMS` của chính Release trên `tsudev-org`,
  không chép tay; Scoop từ chối cài nếu tệp không khớp.
- Workflow `excavator` kiểm Release mới mỗi 6 giờ, **cài thử thật** trên Windows trước khi cập nhật manifest.
- Quy ước đóng gói: [`tsudev-standards/docs/PACKAGING.md`](https://github.com/tsudev-org/tsudev-standards/blob/main/docs/PACKAGING.md).
- Báo lỗ hổng: theo `SECURITY.md` của repo sản phẩm tương ứng, không mở Issue công khai.
