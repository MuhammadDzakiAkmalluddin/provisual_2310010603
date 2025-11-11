-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 11, 2025 at 12:50 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbvisual3_2310010603`
--

-- --------------------------------------------------------

--
-- Table structure for table `arsip`
--

CREATE TABLE `arsip` (
  `IDArsip` bigint NOT NULL,
  `NomorSurat` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Judul` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Tanggal` date DEFAULT NULL,
  `LokasiPenyimpanan` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `arsip`
--

INSERT INTO `arsip` (`IDArsip`, `NomorSurat`, `Judul`, `Tanggal`, `LokasiPenyimpanan`) VALUES
(201, 'SK-01/2025', 'Surat Kuasa Ahmad Fauzan', '2025-01-11', 'Lemari 1 - Map A'),
(202, 'AK-02/2025', 'Akta Perceraian Rina Marlina', '2025-01-20', 'Lemari 1 - Map B'),
(203, 'CT-03/2025', 'Kontrak PT Sumber Rejeki', '2025-02-04', 'Lemari 2 - Map C'),
(204, 'BK-04/2025', 'Bukti Kecelakaan Deni Pratama', '2025-02-11', 'Lemari 3 - Map D'),
(205, 'DW-05/2025', 'Dokumen Waris Siti Maulida', '2025-03-02', 'Lemari 3 - Map E'),
(206, 'SG-06/2025', 'Surat Gugatan CV Barito Makmur', '2025-03-13', 'Lemari 2 - Map F'),
(207, 'LK-07/2025', 'Laporan Keuangan Organisasi', '2025-03-19', 'Lemari 4 - Map G'),
(208, 'DP-08/2025', 'Dokumen Pemalsuan PT KJ', '2025-04-06', 'Lemari 5 - Map H'),
(209, 'PN-09/2025', 'Screenshot Pencemaran Nama', '2025-04-13', 'Lemari 6 - Map I');

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `IDClient` bigint NOT NULL,
  `Nama` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Alamat` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Telepon` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`IDClient`, `Nama`, `Alamat`, `Telepon`, `Email`) VALUES
(1, 'Ahmad Fauzan', 'Jl. A. Yani Km 5 Banjarmasin', '081234567890', 'fauzan@gmail.com'),
(2, 'Rina Marlina', 'Jl. Gatot Subroto No. 12 Banjarbaru', '082145678932', 'rina.m@gmail.com'),
(3, 'PT Sumber Rejeki', 'Jl. Veteran No. 33 Banjarmasin', '081321654987', 'info@sumberrejeki.co.id'),
(4, 'Deni Pratama', 'Jl. Sungai Andai RT 08 Banjarmasin', '081234111222', 'deni_pra@gmail.com'),
(5, 'Siti Maulida', 'Jl. Pramuka Komp. Kertak Hanyar', '081298763445', 'maulida.siti@yahoo.com'),
(6, 'CV Barito Makmur', 'Jl. Pangeran Antasari No. 56', '081276548932', 'admin@baritomakmur.co.id'),
(7, 'Hendra Gunawan', 'Jl. Gubernur Soebardjo No. 19', '081341287654', 'hendragunawan@gmail.com'),
(8, 'PT Kalimantan Jaya', 'Jl. Ahmad Yani Km 10', '081365478921', 'kontak@kalimantanjaya.com'),
(9, 'Nur Aini', 'Jl. Sungai Jingah Banjarmasin', '082178965412', 'nuraini@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `kasus`
--

CREATE TABLE `kasus` (
  `IDKasus` bigint NOT NULL,
  `IDClient` bigint NOT NULL,
  `JudulKasus` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Uraian` text COLLATE utf8mb4_unicode_ci,
  `TanggalMasuk` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `kasus`
--

INSERT INTO `kasus` (`IDKasus`, `IDClient`, `JudulKasus`, `Uraian`, `TanggalMasuk`) VALUES
(101, 1, 'Sengketa Tanah', 'Sengketa kepemilikan tanah antara dua keluarga di Sungai Andai.', '2025-01-10'),
(102, 2, 'Perceraian', 'Permohonan perceraian karena ketidakharmonisan rumah tangga.', '2025-01-15'),
(103, 3, 'Pelanggaran Kontrak', 'PT Sumber Rejeki menggugat mitra karena pelanggaran kontrak kerja sama.', '2025-02-03'),
(104, 4, 'Kecelakaan Kerja', 'Gugatan terhadap perusahaan atas kelalaian keselamatan kerja.', '2025-02-10'),
(105, 5, 'Sengketa Warisan', 'Perselisihan antar saudara mengenai pembagian warisan.', '2025-03-01'),
(106, 6, 'Wanprestasi', 'CV Barito Makmur dituntut karena tidak memenuhi kontrak pengiriman.', '2025-03-12'),
(107, 7, 'Penggelapan Dana', 'Kasus penggelapan dana internal organisasi masyarakat.', '2025-03-18'),
(108, 8, 'Pemalsuan Dokumen', 'Laporan terhadap pihak yang memalsukan dokumen perusahaan.', '2025-04-05');

-- --------------------------------------------------------

--
-- Table structure for table `keuangan`
--

CREATE TABLE `keuangan` (
  `IDKeu` bigint NOT NULL,
  `Tanggal` date NOT NULL,
  `Keterangan` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Jenis` enum('Pemasukan','Pengeluaran') COLLATE utf8mb4_unicode_ci NOT NULL,
  `Jumlah` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `keuangan`
--

INSERT INTO `keuangan` (`IDKeu`, `Tanggal`, `Keterangan`, `Jenis`, `Jumlah`) VALUES
(301, '2025-01-05', 'Pembayaran jasa hukum Ahmad Fauzan', 'Pemasukan', 2500000.00),
(302, '2025-01-12', 'Pembelian alat tulis kantor', 'Pengeluaran', 350000.00),
(303, '2025-01-20', 'Pembayaran jasa perceraian Rina Marlina', 'Pemasukan', 1800000.00),
(304, '2025-02-03', 'Pembelian printer baru', 'Pengeluaran', 1250000.00),
(305, '2025-02-10', 'Pembayaran konsultasi PT Sumber Rejeki', 'Pemasukan', 4000000.00),
(306, '2025-03-01', 'Pembayaran listrik kantor', 'Pengeluaran', 600000.00),
(307, '2025-03-14', 'Pembayaran jasa CV Barito Makmur', 'Pemasukan', 3500000.00),
(308, '2025-03-22', 'Gaji karyawan', 'Pengeluaran', 5000000.00),
(309, '2025-04-10', 'Pembayaran dari PT Kalimantan Jaya', 'Pemasukan', 4500000.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arsip`
--
ALTER TABLE `arsip`
  ADD PRIMARY KEY (`IDArsip`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`IDClient`);

--
-- Indexes for table `kasus`
--
ALTER TABLE `kasus`
  ADD PRIMARY KEY (`IDKasus`),
  ADD KEY `fk_kasus_client` (`IDClient`);

--
-- Indexes for table `keuangan`
--
ALTER TABLE `keuangan`
  ADD PRIMARY KEY (`IDKeu`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kasus`
--
ALTER TABLE `kasus`
  ADD CONSTRAINT `fk_kasus_client` FOREIGN KEY (`IDClient`) REFERENCES `client` (`IDClient`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
